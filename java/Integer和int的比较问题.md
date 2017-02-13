>Integer 在-128 至 127 之间的赋值， Integer 对象是在
IntegerCache.cache 产生，会复用已有对象，这个区间内的 Integer 值可以直接使用==进行
判断，但是这个区间之外的所有数据，都会在堆上产生，并不会复用已有对象，这是一个大坑，
推荐使用 equals 方法进行判断。

        Integer a = 144;
        Integer b = 144;
        if (a == b) {
            System.out.println("a==b");
        } else {
            System.out.println("a <> b");
        }

>上面代码输出 “a <> b”        

        Integer a = 144;
        Integer b = 144;
        if (a.equals(b)) {
            System.out.println("a==b");
        } else {
            System.out.println("a <> b");
        }

>上面代码输出 “a==b”        

>如果是int和Integer混用，则直接用==来判断是没问题的。