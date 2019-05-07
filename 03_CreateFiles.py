# coding=gbk


import os

datas = [{'imgUrl': 'http://ossweb-img.qq.com/images/daoju/zm/detail/16_518.jpg?_t=1544431921', 'imgName': '��ͨ�� ��ޢ'}, {'imgUrl': 'http://ossweb-img.qq.com/images/daoju/zm/detail/16_555.jpg?_t=1528102727', 'imgName': 'Ѫ�۹�Ӱ �ɿ�'}, {'imgUrl': 'http://ossweb-img.qq.com/images/daoju/zm/detail/16_145.jpg?_t=1521095216', 'imgName': '���֮Ů ��ɯ'}, {'imgUrl': 'http://ossweb-img.qq.com/images/daoju/zm/detail/16_142.jpg?_t=1511778558', 'imgName': 'ĺ������ ����'}, {'imgUrl': 'http://ossweb-img.qq.com/images/daoju/zm/detail/16_516.jpg?_t=1503972042', 'imgName': 'ɽ��֮�� �¶�'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_141.jpg', 'imgName': 'Ӱ��֮�� ����'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_497.jpg', 'imgName': '���� ��'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_498.jpg', 'imgName': '���� ϼ'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_164.jpg', 'imgName': '���Ӱ ���۶�'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_427.jpg', 'imgName': '���� ����'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_240.jpg', 'imgName': '��ŭ��ʿ ����'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_163.jpg', 'imgName': '��ȸ ������'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_136.jpg', 'imgName': '�������� ��������������'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_266.jpg', 'imgName': '���ὣħ ���п�˹'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_30.jpg', 'imgName': '�����̳��� ������˹'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_3.jpg', 'imgName': '������� �����'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_202.jpg', 'imgName': 'Ϸ��ʦ ��'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_420.jpg', 'imgName': '���޼�˾ ������'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_203.jpg', 'imgName': '����˫�� ǧ��'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_41.jpg', 'imgName': '����֮�� ���ʿ�'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_223.jpg', 'imgName': '����֮�� ��ķ'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_245.jpg', 'imgName': 'ʱ��̿� ����'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_432.jpg', 'imgName': '�ǽ����� �͵�'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_421.jpg', 'imgName': '��նݵ��� �׿���'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_429.jpg', 'imgName': '����֮ì ����˿��'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_268.jpg', 'imgName': 'ɳĮ�ʵ� ���ȶ�'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_150.jpg', 'imgName': '��ʧ֮�� �ɶ�'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_127.jpg', 'imgName': '��˪Ů�� ��ɣ׿'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_86.jpg', 'imgName': '��������֮�� ����'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_201.jpg', 'imgName': '���׶�׿��֮�� ��¡'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_161.jpg', 'imgName': '���֮�� ά����'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_157.jpg', 'imgName': '���罣�� ����'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_222.jpg', 'imgName': '�������� ���˿'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_236.jpg', 'imgName': 'ʥǹ���� ¬����'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_154.jpg', 'imgName': '����ħ�� ����'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_133.jpg', 'imgName': '��������֮�� ����'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_412.jpg', 'imgName': '���������� ��ʯ'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_254.jpg', 'imgName': 'Ƥ��ִ���� ε'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_267.jpg', 'imgName': '�����޼� ����'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_238.jpg', 'imgName': 'Ӱ��֮�� ��'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_60.jpg', 'imgName': '֩��Ů�� ����˿'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_121.jpg', 'imgName': '����Ӷ��� ���ȿ�'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_134.jpg', 'imgName': '����Ԫ�� ������'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_107.jpg', 'imgName': '��֮׷���� �׶��Ӷ�'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_131.jpg', 'imgName': '���Ů�� �찲��'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_143.jpg', 'imgName': '����֮�� ���'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_126.jpg', 'imgName': 'δ���ػ��� ��˹'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_119.jpg', 'imgName': '��ҫ���̹� ������'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_122.jpg', 'imgName': 'ŵ����˹֮�� ������˹'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_110.jpg', 'imgName': '�ͽ�֮�� Τ³˹'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_120.jpg', 'imgName': 'ս��֮Ӱ �տ���ķ'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_117.jpg', 'imgName': '����Ů�� ��'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_114.jpg', 'imgName': '��˫���� �ư���'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_111.jpg', 'imgName': '�̩̹ ŵ����˹'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_115.jpg', 'imgName': '���ƹ��� ����˹'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_113.jpg', 'imgName': '����֮ŭ ɪׯ��'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_112.jpg', 'imgName': '��е���� ά����'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_103.jpg', 'imgName': '��β���� ����'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_106.jpg', 'imgName': '�������� ��������'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_101.jpg', 'imgName': 'Զ������ ����˹'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_105.jpg', 'imgName': '��ϫ���� ����'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_102.jpg', 'imgName': '��Ѫ�伧 ϣ����'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_104.jpg', 'imgName': '�����ͽ ���׸�˹'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_91.jpg', 'imgName': '����֮Ӱ ̩¡'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_92.jpg', 'imgName': '����֮�� ����'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_72.jpg', 'imgName': 'ˮ���ȷ� ˹����'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_89.jpg', 'imgName': '���Ů�� ��ŷ��'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_62.jpg', 'imgName': '�����ʥ �����'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_83.jpg', 'imgName': '������ Լ���'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_61.jpg', 'imgName': '����ħ�� ������'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_67.jpg', 'imgName': '��ҹ���� ޱ��'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_68.jpg', 'imgName': '��е���� ����'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_56.jpg', 'imgName': '�������� ħ��'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_64.jpg', 'imgName': 'äɮ ����'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_63.jpg', 'imgName': '������� ������'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_59.jpg', 'imgName': '�������ǻ��� ��������'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_43.jpg', 'imgName': '������ ������'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_57.jpg', 'imgName': 'Ť������ ï��'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_58.jpg', 'imgName': '��Į���� �׿˶�'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_51.jpg', 'imgName': 'Ƥ��Ů�� ������'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_69.jpg', 'imgName': 'ħ��֮ӵ ���������'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_7.jpg', 'imgName': '�������� ��ܽ��'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_48.jpg', 'imgName': '��ħ֮�� ���ʵ¶�'}, {'imgUrl': 'http://ossweb-img.qq.com/images/daoju/zm/detail/16_39000.jpg?_t=1523326526', 'imgName': '�������� �������'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_98.jpg', 'imgName': 'ĺ��֮�� ��'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_33.jpg', 'imgName': '�������� ��Ī˹'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_1.jpg', 'imgName': '�ڰ�֮Ů ����'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_2.jpg', 'imgName': '��սʿ ������'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_4.jpg', 'imgName': '���ƴ�ʦ ��˹��'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_5.jpg', 'imgName': '�°��ܹ� ����'}, {'imgUrl': 'http://ossweb-img.qq.com/images/daoju/zm/detail/16_6.jpg?_t=1501760364', 'imgName': '��ηս�� �����'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_8.jpg', 'imgName': '�ɺ��ո��� �������׶�'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_9.jpg', 'imgName': 'ĩ��ʹ�� �ѵ����'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_10.jpg', 'imgName': '������ʹ ����'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_12.jpg', 'imgName': 'ţͷ���� ����˹��'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_13.jpg', 'imgName': '���ķ�ʦ ����'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_15.jpg', 'imgName': 'ս��Ů�� ϣά��'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_16.jpg', 'imgName': '����֮�� ������'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_17.jpg', 'imgName': 'Ѹ�ݳ�� ��Ī'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_18.jpg', 'imgName': '�������� ��˿����'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_19.jpg', 'imgName': '�氲ŭ�� �����'}, {'imgUrl': 'http://ossweb-img.qq.com/images/daoju/zm/detail/16_20.jpg?_t=1536117011', 'imgName': 'ѩԭ˫�� ŬŬ��������'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_21.jpg', 'imgName': '�ͽ����� ����С��'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_23.jpg', 'imgName': '����֮�� ̩���׶�'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_25.jpg', 'imgName': '������ʹ Ī����'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_26.jpg', 'imgName': 'ʱ���ػ��� ����'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_27.jpg', 'imgName': '������ʿ ������'}, {'imgUrl': 'http://ossweb-img.qq.com/images/daoju/zm/detail/16_28_1.jpg?_t=1508220875', 'imgName': 'ʹ��֮ӵ ��ܽ��'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_29.jpg', 'imgName': '����֮Դ ͼ��'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_32.jpg', 'imgName': '��֮ľ���� ��ľľ'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_34.jpg', 'imgName': '������� ����ά��'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_36.jpg', 'imgName': '�氲���� �ɶ�'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_37.jpg', 'imgName': '��ɪ��Ů ���'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_38.jpg', 'imgName': '������� ������'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_40.jpg', 'imgName': '�籩֮ŭ ����'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_42.jpg', 'imgName': 'Ӣ��Ͷ���� ����'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_44.jpg', 'imgName': '������֮�� �����'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_45.jpg', 'imgName': 'а��С��ʦ ά��'}, {'imgUrl': 'http://ossweb-img.qq.com/images/daoju/zm/detail/17_50.jpg?_t=1519811517', 'imgName': 'ŵ����˹ͳ�� ˹ά��'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_53.jpg', 'imgName': '���������� �����'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_54.jpg', 'imgName': '���Ҿ��� ī����'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_55.jpg', 'imgName': '����֮�� ��������'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_75.jpg', 'imgName': 'ɳĮ���� ��ɪ˹'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_76.jpg', 'imgName': '��ҰŮ���� �ε���'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_77.jpg', 'imgName': '�������� �ڵ϶�'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_78.jpg', 'imgName': 'ʥ��֮�� ����'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_79.jpg', 'imgName': '��Ͱ ������˹'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_80.jpg', 'imgName': 'ս��֮�� ��ɭ'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_81.jpg', 'imgName': '̽�ռ� �������'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_82.jpg', 'imgName': '����ڤ�� Ī�¿���'}, {'imgUrl': 'http://ossweb-img.qq.com/images/daoju/zm/detail/16_84.jpg?_t=1533538637', 'imgName': '��Ⱥ֮�� ������'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_85.jpg', 'imgName': '��֮�� ����'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_90.jpg', 'imgName': '�����֪ �������'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_96.jpg', 'imgName': '��Ԩ�޿� �˸�Ī'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_14.jpg', 'imgName': '����ս�� ����'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_11.jpg', 'imgName': '�޼���ʥ ��'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_74.jpg', 'imgName': '������ ��Ĭ����'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_99.jpg', 'imgName': '���Ů�� ����˿'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_35.jpg', 'imgName': '��ħС�� ����'}, {'imgUrl': 'https://ossweb-img.qq.com/images/daoju/zm/detail/16_31.jpg', 'imgName': '��տ־� �Ƽ�˹'}]

def createFiles(filePath):
    isExists=os.path.exists(filePath)
    if not isExists:
        os.makedirs(filePath)

path = 'D:\\�����ļ���\\'
for dic in datas:
    createFiles(path+dic['imgName'])
