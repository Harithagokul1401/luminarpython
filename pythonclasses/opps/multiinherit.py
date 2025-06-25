class parent():
    def m1(self):
        print("inside parent")

class child(parent):
    def m2(self):
        print("inside chid")

class subchild(child):
    def m3(self):
        print("inside subchild")


# agar parent ka object hai tuh sirf m1 call hoga
# agar child ka object hai tuh m1 and m2 call hoga
# agar subchild ka object hai tuh m1,m22,m3 call hoga

obj=subchild()
obj.m1()
obj.m2()
obj.m3()

# 2 example

# class parent():
#     def m1(self):
#         print("inside parent")

# class child():
#     def m1(self):
#         print("inside chid")

# class subchild(child,parent):  # in java there is a conflict as both has m1()but here python give priority to first one
#     def m3(self):
#         print("inside subchild")

# obj = subchild()
# obj.m1() # child ka m1 hoga call kyuki line 32 me first child likhahai bracket me ..
#          #if class subchild(parent,child): aaisa hota tuh parent ka m1 hoga call
# obj.m3() # subchild ka function


