function xyz = dis_to_pos_matlab(x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,da,db,dc,dd)

% �趨��վ��ֵ
% A=[0,0,0];
% B=[0,8,0];
% C=[6,0,0];
% D=[0,0,3];
A=[x1,x2,x3];
B=[x4,x5,x6];
C=[x7,x8,x9];
D=[x10,x11,x12];

% �趨��ǩ��ֵ
%length(rtlength);%�˴�ֱ�Ӿ���1
%xyz=zeros(3,length(rtlength));
xyz=zeros(3,1);

% �趨��ǩ��ֵ
% data=rand(1000,3)*10;%��������(0, 1)֮����ȷֲ����������ɵ�����,1000*3
% data(:,1) = rand(1000,1)*6;
% data(:,2) = rand(1000,1)*8;
% data(:,3) = rand(1000,1)*3;

% rtlength ÿһ��Ϊ�㵽4����վ�ľ���
%length(data);%ĳdata��������ά����󳤶ȡ����˴�ֱ�Ӿ���1
%rtlength =zeros(length(data),4);

rtlength = [da,db,dc,dd];

% for t=1:length(data)
%     rtlength(t,1) =sqrt((data(t,1)-A(1))^2+(data(t,2)-A(2))^2+(data(t,3)-A(3))^2);%�ھ��������һ����������(rand(1)-0.5)*1
%     rtlength(t,2) =sqrt((data(t,1)-B(1))^2+(data(t,2)-B(2))^2+(data(t,3)-B(3))^2); 
%     rtlength(t,3) =sqrt((data(t,1)-C(1))^2+(data(t,2)-C(2))^2+(data(t,3)-C(3))^2);
%     rtlength(t,4) =sqrt((data(t,1)-D(1))^2+(data(t,2)-D(2))^2+(data(t,3)-D(3))^2);
% end
     
%plot3(data(:,1),data(:,2),data(:,3),'.');
%hold on %�����ͼ�����߻�����ͬһ��ͼ����
% plot3(xyz(1,1),xyz(2,1),xyz(3,1),'*b');
% hold on
% plot3(A(1),A(2),A(3),'*r');
% plot3(B(1),B(2),B(3),'*r');
% plot3(C(1),C(2),C(3),'*r');
% plot3(D(1),D(2),D(3),'*r');
% axis ([0 6 0 8 0 3])%axis([xmin,xmax,ymin,ymax,zmin,zmax])
% grid on;%���������

%for h=1:length(rtlength)
%               AP =[0,0,0
%                   0,8,0
%                   6,0,0
%                   0,0,3] ;
              AP =[x1,x2,x3
                  x4,x5,x6
                  x7,x8,x9
                  x10,x11,x12] ;
              num_ap = length(AP);
              if num_ap>=4
              Q =zeros(1,num_ap);
              for j=1:num_ap
                 Q(1,j) =0.5;
              end
               Q = diag(Q);%���ɶԽǾ���
              for i=1:num_ap     
                  Node(i)=AP(i,1)^2+AP(i,2)^2+AP(i,3)^2;    %�̶���������λ�ù���
              end
              A=[];b=[];
%               L =rtlength(h,:);       %TOA���
              L =rtlength(1,:);       %TOA���
              for i=1:num_ap             %���߶�λ��ʽ��һ����ɾ���A*x=b
                  A=[A;2*(AP(i,1)-AP(1,1)),2*(AP(i,2)-AP(1,2)),2*(AP(i,3)-AP(1,3))];  %ϵ������A
                  b=[b;L(1)^2-L(i)^2+Node(i)-Node(1)];      %�������b
              end
               x=inv(A'*inv(Q)*A)*(A'*inv(Q)*b);      %������С���˷����Ŀ�ĵ�����λ��
%                xyz(:,h)=x;
               xyz(:,1)=x;
%                sprintf('%2.2f%%', (line/bg)*100)    %%2.2f�Ǳ���2λС���ˣ�Ҳ����ֱ��д%f
              end
%end
end