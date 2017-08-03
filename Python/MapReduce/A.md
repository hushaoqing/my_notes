## MapReduce

* 创建一个Map函数处理一个基于key/value pair的数据集合，
* 输出中间的基于key/value pair的数据集合；
* 然后再创建一个Reduce函数用来合并所有的具有相同中间key值的中间value值

MapReduce架构的程序能够在大量的普通配置的计算机上实现并行化处理。这个系统在运行时只关心：

* 如何分割输入数据，
* 在大量计算机组成的集群上的调度，
* 集群中计算机的错误处理，
* 管理集群中计算机之间必要的通信。

采用MapReduce架构可以使那些没有并行计算和分布式处理系统开发经验的程序员有效利用分布式系统的丰富资源。


设计这个抽象模型的灵感来自Lisp和许多其他函数式语言的Map和Reduce的原语。我们意识到我们大多数的运算都包含这样的操作：在输入数据的“逻辑”记录上应用Map操作得出一个中间key/value pair集合，然后在所有具有相同key值的value值上应用Reduce操作，从而达到合并中间的数据，得到一个想要的结果的目的。使用MapReduce模型，再结合用户实现的Map和Reduce函数，我们就可以非常容易的实现大规模并行化计算；通过MapReduce模型自带的“再次执行”（re-execution）功能，也提供了初级的容灾实现方案。


1. 用户程序首先调用的MapReduce库将输入文件分成M个数据片度，每个数据片段的大小一般从 16MB到64MB(可以通过可选的参数来控制每个数据片段的大小)。然后用户程序在机群中创建大量的程序副本。
2. 这些程序副本中的有一个特殊的程序–master。副本中其它的程序都是worker程序，由master分配任务。有M个Map任务和R个Reduce任务将被分配，master将一个Map任务或Reduce任务分配给一个空闲的worker。
3. 被分配了map任务的worker程序读取相关的输入数据片段，从输入的数据片段中解析出key/value pair，然后把key/value pair传递给用户自定义的Map函数，由Map函数生成并输出的中间key/value pair，并缓存在`内存`中。
4. 缓存中的key/value pair通过分区函数分成R个区域，之后周期性的`写入到本地磁盘`上。缓存的key/value pair在本地磁盘上的存储位置将被回传给master，由master负责把这些存储位置再传送给Reduce worker。
5. 当Reduce worker程序接收到master程序发来的`数据存储位置信息`后，使用`RPC`从Map worker所在主机的磁盘上读取这些缓存数据。当Reduce worker读取了所有的中间数据后，通过对key进行`排序`后使得具有相同key值的数据聚合在一起。由于许多不同的key值会映射到相同的Reduce任务上，因此`必须进行排序`。如果中间数据太大无法在内存中完成排序，那么就要在外部进行排序。
6. Reduce worker程序遍历排序后的中间数据，对于每一个唯一的中间key值，Reduce worker程序将这个key值和它相关的中间value值的集合传递给用户自定义的Reduce函数。Reduce函数的输出被追加到所属分区的输出文件。
7. 当所有的Map和Reduce任务都完成之后，master`唤醒用户程序`。在这个时候，在用户程序里的对MapReduce调用才`返回`。

to be continued..