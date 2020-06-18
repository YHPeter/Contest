# YACS 2020.6乙组#1.py
'''
给定 mm 条修改操作，请模拟编辑器在这些操作下的行为，最后输出编辑器所记录的文本内容：

前进操作：编辑器将光标向右移动一格，如果光标已经在最右端，则忽略这步操作；
后退操作：编辑器将光标向左移动一格，如果光标已经在最左端，则忽略这步操作；
插入操作：该操作还需要提供一个字符参数 ch，编辑器在光标的左侧插入该字符；
删除操作：文本编辑器将删去光标右侧的字符，若光标右侧没有字符，则忽略这步操作。
输入格式
第一行：单个整数 mm；
第二行到第 m+1m+1 行：每行表示一个操作；

前进操作仅有一个字母 f。
后退操作仅有一个字母 b；
删除操作仅有一个字母 d；
插入操作以字母 i 开头，后接一个字母，保证该字母是一个大写的英文字母， i 和该字母中间用一个空格分隔。
'''

import array,itertools
class gapbuffer(object):
    TYPE_CODES = {"u": ('a', "unicode character")}
    def __init__(self, typecode, initial_content=[], gap_size=10000):
        self.gap_size = gap_size
        item = gapbuffer.TYPE_CODES[typecode][0]
        self.__buf = array.array(typecode, (item for i in range(gap_size)))
        self.__gap_start = 0
        self.__gap_end = len(self.__buf)
        self.__content_end = len(self.__buf)
    @property
    def typecode(self):
        return self.__buf.typecode
    @property
    def __gap_len(self):
        return self.__gap_end - self.__gap_start
    def __len__(self):
        return self.__content_end - self.__gap_len
    def __compare(self, other):
        if not hasattr(other, "__len__"):
            return 1
        fv = object()
        for si, oi in itertools.izip_longest(self, other, fillvalue=fv):
            if si is fv:
                return -1
            if oi is fv:
                return 1            
            if oi > si:
                return -1
            elif oi < si:
                return 1
        return 0
    def __enforce_index(self, *indices):
        for index in indices:
            if index >= len(self) or index < -len(self):
                raise IndexError(self.__class__.__name__ + " index out of range")
    def __getitem__(self, x):
        if isinstance(x, slice):
            return self.__get_slice(x)
        return self.__get_index(x)
    def __get_index(self, i):
        self.__enforce_index(i)
        index = i if i < self.__gap_start else i + self.__gap_len
        return self.__buf[index]
    def __get_slice(self, s):
        return gapbuffer(self.typecode,
                (self[i] for i in range(*s.indices(len(self)))))
    def __setitem__(self, x, value):
        if isinstance(x, slice):
            return self.__set_slice(x, value)
        return self.__set_index(x, value)
    def __set_index(self, i, value):
        self.__enforce_index(i)
        index = i if i < self.__gap_start else i + self.__gap_len
        self.__buf[index] = value
    def __set_slice(self, s, value):
        values = value
        if not hasattr(value, "__len__"):
            values = [v for v in value]
        start, stop, step = s.indices(len(self))
        if step != 1:
            xr = range(start, stop, step)
            if len(values) != len(xr):
                pass
            for i, v in itertools.izip(xr, values):
                self[i] = v
        else:
            self.__move_gap(start)
            self.__resize_gap(len(values))
            self.__gap_end += stop - start
            for v in values:
                self.__buf[self.__gap_start] = v
                self.__gap_start += 1
    def __delitem__(self, x):
        if isinstance(x, slice):
            return self.__del_slice(x)
        return self.__del_index(x)
    def __del_index(self, i):
        self.__enforce_index(i)
        self.__move_gap(i)
        self.__gap_end += 1
    def insert(self, index, item):
        self[index:index] = [item]
    def pop(self, index):
        index = len(self) - 1 if index is None else index
        item = self[index]
        del self[index]
        return item
    def __resize_gap(self, target_size):
        if self.__gap_len < target_size:
            gap_delta = target_size + self.gap_size - self.__gap_len
            self.__resize_buf(len(self.__buf) + gap_delta)
            for i in reversed(range(self.__gap_end, self.__content_end)):
                self.__buf[i + gap_delta] = self.__buf[i]
            self.__gap_end += gap_delta
            self.__content_end += gap_delta
    def __move_gap(self, index):
        if len(self) == 0:
            return
        index = len(self) + index if index < 0 else index
        assert 0 <= index <= len(self)
        if self.__gap_len == 0:
            self.__gap_start = self.__gap_end = index
        else:
            while self.__gap_start > index:
                self.__gap_start -= 1
                self.__gap_end -= 1
                self.__buf[self.__gap_end] = self.__buf[self.__gap_start]
            while self.__gap_start < index:
                self.__buf[self.__gap_start] = self.__buf[self.__gap_end]
                self.__gap_start += 1
                self.__gap_end += 1
    def __str__(self):
        if self.typecode in ["u", "c"]:
            return ''.join(c for c in self)
        return repr([i for i in self])
m = 0
t = gapbuffer("u", "")
for _ in range(int(input())):
    act = input().split(' ')
    if act[0]=='f':
        m = min(len(t),m+1)
    elif act[0]=='b':
        m = max(0,m-1)
    elif act[0]=='d':
        try:
            t.pop(m)
        except: continue
    elif act[0]=='i':
        t.insert(m,act[1])
        m+=1
print(t)