## Leetcode code

```
# !usr/bin/python
# coding=utf-8

import math, copy, collections, re, operator

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        <self class="ri"></self>ght = None

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    """
    leetcode solution

    447. Number of Boomerangs
    268. Missing Number
    541. Reverse String II
    350. Intersection of Two Arrays II
    206. Reverse Linked List
    13.  Roman to Integer
    217. Contains Duplicate
    401. Binary Watch
    409. Longest Palindrome
    242. Valid Anagram
    169. Majority Element
    100. Same Tree
    237. Delete Node in a Linked List
    171. Excel Sheet Column Number
    387. First Unique Character in a String
    349. Intersection of Two Arrays
    504. Base 7
    404. Sum of Left Leaves
    383. Ransom Note
    453. Minimum Moves to Equal Array Elements
    455. Assign Cookies
    167. Two Sum II - Input array is sorted
    283. Move Zeroes
    506. Relative Ranks
    492. Construct the Rectangle
    389. Find the Difference
    136. Single Number
    448. Find All Numbers Disappeared in an Array
    520. Detect Capital
    292. Nim Game
    344. Reverse String
    412. Fizz Buzz
    496. Next Greater Element I
    500. Keyboard Row
    476. Number Complement
    461. Hamming Distance
    486. findMaxConsecutiveOnes
    463. islandPerimeter
    """
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res = 0
        for p in points:
            cmap = {}
            for q in points:
                f = p[0]-q[0]
                s = p[1]-q[1]
                cmap[f*f + s*s] = 1 + cmap.get(f*f + s*s, 0)
            for k in cmap:
                res += cmap[k] * (cmap[k] -1)
        return res

    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        return n * (n+1) / 2 - sum(nums)

    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = "abcdefg"
        k = 3
        t = ""
        for i, x in enumerate(list(s)[::2*k]):
            i = i * 2 * k
            t += s[i:i+k][::-1] + s[i+k:i+2*k]
        return t


    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list((collections.Counter(nums1) & collections.Counter(nums2)).elements())
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
        z = 0
        for i in range(0, len(s) - 1):
            if roman[s[i]] < roman[s[i+1]]:
                z -= roman[s[i]]
            else:
                z += roman[s[i]]
        return z + roman[s[-1]]

    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) != len(set(nums))
        ###
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:continue
                if nums[i] == nums[j]:
                    return True
        return True
        ###
        if len(nums) < 2: return False
        for x in collections.Counter(nums).values():
            if x != 1:
                return True
        return False

    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """

        return ['%d:%02d' % (h, m)
            for h in range(12) for m in range(60)
            if (bin(h) + bin(m)).count('1') == num]

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """

        for x in collections.Counter(s).values():
            print x & 1
        odds = sum(v & 1 for v in collections.Counter(s).values())
        return len(s) - odds + bool(odds)
        ###
        t = 0
        tag = False
        if len(collections.Counter(s)) == 1: return len(s)
        for x in collections.Counter(s).iteritems():
            if x[1] == 1:tag = True
            if x[1] > 1:
                if x[1] % 2 == 0:
                    t += x[1]
                else:
                    t += x[1] - 1
                    tag = True
        return t + 1 if tag else t

    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return collections.Counter(s) == collections.Counter(t)

    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        t = len(nums) // 2
        for i in collections.Counter(nums).iteritems():
            if i[1] > t:
                return i[0]

    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return p is q

    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next

    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = "B"
        conve = lambda x,y: (ord(x) - 64) - (ord(y) - 64) + 1
        su = 0
        for i, x in enumerate(list(s)[::-1]):
            su += conve(x, "A") * math.pow(26, i)
        return int(su)

    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        list_a = []
        for c,v in collections.Counter(s).iteritems():
            if v == 1:
                list_a.append(s.find(c))
        return min(list_a or [-1])

    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list(set(nums1).intersection(set(nums2)))

    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num < 0: return '-' + self.convertToBase7(-num)
        if num < 7: return str(num)
        return self.convertToBase7(num // 7) + str(num % 7)

        if num == 0: return "0"
        num_d = abs(num)
        s = []
        while num_d != 0:
            s.append(num_d % 7)
            num_d = num_d // 7
        t = "".join([str(x) for x in s[::-1]])
        return t if num > 0 else "-" + t
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:return 0
        if root.left and not root.left.left and not root.left.right:
            return root.left.val + self.sumOfLeftLeaves(root.right)
        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)

    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        return not collections.Counter(ransomNote) - collections.Counter(magazine)

        if not ransomNote:
            return True
        if not magazine:
            return False
        tag = False
        s = list(magazine)
        for x in list(ransomNote):
            if x in s:
                tag = True
                s.remove(x)
            else:
                return False
        return tag


    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(nums) - len(nums) * min(nums)
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """

        g.sort()
        s.sort()
        i, j = 0, 0
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                i += 1
            j += 1
        return i

        g.sort()
        s.sort()
        t = 0
        for i in g:
            for j in s:
                if j >= i:
                    t += 1
                    s.remove(j)
                    break
        return t

    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i, num in enumerate(numbers):
            if target - num in dic:
                return [dic[target-num]+1, i+1]
            dic[num] = i

        ######### time limit
        # print numbers
        # a = []
        # for num, v in enumerate(numbers):
        #     t = target - v
        #     if t in numbers:
        #         for i, s in enumerate(numbers):
        #             if s == t:
        #                 a.append((i + 1, s))
        #         l = [(num + 1, v)]
        #         r = a
        #         ret = [ i for i in r if i not in l]
        #         return numbers.index(v) + 1, ret[0][0]

    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        zero = 0  # records the position of "0"
        for i in xrange(len(nums)):
            if nums[i] != 0:
                print i, zero
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1
            # print zero
            print nums
        for i, x in enumerate(nums):
            if i == len(nums):
                break
            if x == 0:
                nums.remove(x)
                nums.append(0)

    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        print nums
        s = sorted(nums)
        print s[::-1]
        ss = copy.deepcopy(nums)
        for num, v in enumerate(s[::-1]):
            ind = nums.index(v)
            ss[ind] = num
        print ss
        a = []
        for i in ss:
            if i == 0:
                a.append("Gold Medal")
            elif i == 1:
                a.append("Silver Medal")
            elif i == 2:
                a.append("Bronze Medal")
            else:
                a.append(str(i + 1))
        return a

    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """

        mid = int(math.sqrt(area))
        while mid > 0:
            if area % mid == 0:
                return [int(area / mid), int(mid)]
            mid -= 1
        tag = area * 2
        s = [0, 0]
        for w in range(1, area + 1):
            if area % w == 0:
                l = area / w
                if l >= w and l + w <= tag:
                    tag =  l + w
                    s = [l, w]
        return s



    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        return chr(reduce(operator.xor, map(ord, s + t)))

        from collections import Counter
        a = Counter(s)
        b = Counter(t)
        for i in b.items():
            if i not in a.items():
                return i[0]
        # return list(b - a)[0]
    def singleNumber(self, s):
        """
        :type s: List[int]
        :rtype: int
        """

        t = 0
        for i, v in enumerate(s):
            for j, k in enumerate(s):
                if i == j:
                    continue
                elif v == k:
                    break
                else:
                    continue
            if j == len(s) - 1:
                t = v
        return t

        res = 0
        for n in s:
            res ^= n
        return res

    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        print nums
        for n in nums:
            nums[abs(n) - 1] = -abs(nums[abs(n) - 1])
            print nums
        print nums
        return [i + 1 for i, n in enumerate(nums) if n > 0]


    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        #  [A-Z]+|[a-z]+|[A-Z][a-z]+
        return word.islower() or word.istitle() or word.isupper()

    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n % 4 != 0
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        a = []
        for n in range(1, n + 1):
            q = n % 3
            w = n % 5
            if q == 0 and w == 0:
                a.append("FizzBuzz")
            elif w == 0:
                a.append("Buzz")
            elif q == 0:
                a.append("Fizz")
            else:
                a.append(str(n))
        return a
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        a = []
        for x in findNums:
            if x == nums[-1]:
                tt = [x]
            else:
                ind = nums.index(x) + 1
                tt = nums[ind:]
            for i in tt:
                if x >= i:
                    t = -1
                else:
                    t = i
                    break
            a.append(t)
        return a
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        Q = "QWERTYUIOPqwertyuiop"
        A = "ASDFGHJKLasdfghjkl"
        Z = "ZXCVBNMzxcvbnm"

        def check(s, tag):
            for i in list(s):
                if i in tag:
                    continue
                else:
                    return False
            return True
        s = []
        for st in words:
            if check(st, Q) or check(st, A) or check(st, Z):
                s.append(st)
        return s
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        i = 1
        while i <= num:
            num ^= i
            i <<= 1
        return num
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return bin(x ^ y).count("1")

    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        data = [1,1,0,1,1,1]
        """
        list_a = []
        su = 0
        s = 0
        for n in nums:
            s += n
            if s > su:
                list_a.append(s)
                su = s
            else:
                s = 0
                su = 0
        return max(list_a) if list_a else 0



    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int

        data = [[0, 1, 0, 0],
          [1, 1, 1, 0],
          [0, 1, 0, 0],
          [1, 1, 0, 0]]
        data = [[1, 1]]
        """
        def deal(lis, i, grid, r):
            a = []
            l = lis[i - 1] if i - 1 >= 0 else 0
            right = lis[i + 1] if i + 1 < len(lis) else 0
            u = grid[r - 1][i] if r - 1 >= 0 else 0
            d = grid[r + 1][i] if r + 1 < len(grid) else 0
            print i, r, l, right, u, d
            a.append(l)
            a.append(r)
            a.append(u)
            a.append(d)
            s = a.count(1)
            return 4 - s
        a = 0
        for r, row in enumerate(grid):
            for i, l in enumerate(row):
                if l == 1:
                    a += deal(row, i, grid, r)
        return a

if __name__ == '__main__':
    l = Solution()
    print l.reverseStr("abcdef", 2)
```