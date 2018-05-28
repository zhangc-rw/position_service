function xyz = dis_to_pos_matlab(x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,da,db,dc,dd)

% 设定基站的值
% A=[0,0,0];
% B=[0,8,0];
% C=[6,0,0];
% D=[0,0,3];
A=[x1,x2,x3];
B=[x4,x5,x6];
C=[x7,x8,x9];
D=[x10,x11,x12];

% 设定标签的值
%length(rtlength);%此处直接就是1
%xyz=zeros(3,length(rtlength));
xyz=zeros(3,1);

% 设定标签的值
% data=rand(1000,3)*10;%产生由在(0, 1)之间均匀分布的随机数组成的数组,1000*3
% data(:,1) = rand(1000,1)*6;
% data(:,2) = rand(1000,1)*8;
% data(:,3) = rand(1000,1)*3;

% rtlength 每一行为点到4个基站的距离
%length(data);%某data矩阵所有维的最大长度——此处直接就是1
%rtlength =zeros(length(data),4);

rtlength = [da,db,dc,dd];

% for t=1:length(data)
%     rtlength(t,1) =sqrt((data(t,1)-A(1))^2+(data(t,2)-A(2))^2+(data(t,3)-A(3))^2);%在距离上添加一定的随机误差(rand(1)-0.5)*1
%     rtlength(t,2) =sqrt((data(t,1)-B(1))^2+(data(t,2)-B(2))^2+(data(t,3)-B(3))^2); 
%     rtlength(t,3) =sqrt((data(t,1)-C(1))^2+(data(t,2)-C(2))^2+(data(t,3)-C(3))^2);
%     rtlength(t,4) =sqrt((data(t,1)-D(1))^2+(data(t,2)-D(2))^2+(data(t,3)-D(3))^2);
% end
     
%plot3(data(:,1),data(:,2),data(:,3),'.');
%hold on %将多幅图的曲线绘制在同一个图形上
% plot3(xyz(1,1),xyz(2,1),xyz(3,1),'*b');
% hold on
% plot3(A(1),A(2),A(3),'*r');
% plot3(B(1),B(2),B(3),'*r');
% plot3(C(1),C(2),C(3),'*r');
% plot3(D(1),D(2),D(3),'*r');
% axis ([0 6 0 8 0 3])%axis([xmin,xmax,ymin,ymax,zmin,zmax])
% grid on;%添加网格线

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
               Q = diag(Q);%生成对角矩阵
              for i=1:num_ap     
                  Node(i)=AP(i,1)^2+AP(i,2)^2+AP(i,3)^2;    %固定参数便于位置估计
              end
              A=[];b=[];
%               L =rtlength(h,:);       %TOA测距
              L =rtlength(1,:);       %TOA测距
              for i=1:num_ap             %三边定位公式逐一作差化成矩阵：A*x=b
                  A=[A;2*(AP(i,1)-AP(1,1)),2*(AP(i,2)-AP(1,2)),2*(AP(i,3)-AP(1,3))];  %系数矩阵A
                  b=[b;L(1)^2-L(i)^2+Node(i)-Node(1)];      %增广矩阵b
              end
               x=inv(A'*inv(Q)*A)*(A'*inv(Q)*b);      %利用最小二乘法求解目的点坐标位置
%                xyz(:,h)=x;
               xyz(:,1)=x;
%                sprintf('%2.2f%%', (line/bg)*100)    %%2.2f是保留2位小数了，也可以直接写%f
              end
%end
end