>在涉及循环中删除列表里面的数据时，要用Iterator 迭代器来进行 否则会报错

> 对于add操作，则在整个迭代器迭代过程中是不允许的。 其他集合(Map/Set)使用迭代器迭代也是一样。
   
        List<String> a = new ArrayList<String>();
        a.add("1");
        a.add("2");
        System.out.println(a.toString());
        //      for (String tmp:a) {
        //          if ("2".equals(tmp)) {
        //              a.remove(tmp); //报错   java.util.ConcurrentModificationException
        //          }
        //      }
        Iterator<String> i = a.iterator();
        while (i.hasNext()) {
            String tmp = i.next();
            if ("2".equals(tmp)) {
                i.remove();
            }
        }
        System.out.println(a.toString());