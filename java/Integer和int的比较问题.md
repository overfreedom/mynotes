>Integer ��-128 �� 127 ֮��ĸ�ֵ�� Integer ��������
IntegerCache.cache �������Ḵ�����ж�����������ڵ� Integer ֵ����ֱ��ʹ��==����
�жϣ������������֮����������ݣ������ڶ��ϲ����������Ḵ�����ж�������һ����ӣ�
�Ƽ�ʹ�� equals ���������жϡ�

        Integer a = 144;
        Integer b = 144;
        if (a == b) {
            System.out.println("a==b");
        } else {
            System.out.println("a <> b");
        }

>���������� ��a <> b��        

        Integer a = 144;
        Integer b = 144;
        if (a.equals(b)) {
            System.out.println("a==b");
        } else {
            System.out.println("a <> b");
        }

>���������� ��a==b��        

>�����int��Integer���ã���ֱ����==���ж���û����ġ�