>���漰ѭ����ɾ���б����������ʱ��Ҫ��Iterator ������������ ����ᱨ��

> ����add�������������������������������ǲ�����ġ� ��������(Map/Set)ʹ�õ���������Ҳ��һ����
   
        List<String> a = new ArrayList<String>();
        a.add("1");
        a.add("2");
        System.out.println(a.toString());
        //      for (String tmp:a) {
        //          if ("2".equals(tmp)) {
        //              a.remove(tmp); //����   java.util.ConcurrentModificationException
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