 write('vvedi levuyu granicu  '); readln(a);
 write('vvedi pravuyu granicu  '); readln(b);
 write('vvedi eps '); readln(e);
 k:=0;
  if f(a)*f2(a)>0 then x0:=a else x0:=b;

     x1:=x0-f(x0)/f1(x0);
     x2:=a-((b-a)*f(a)/(f(b)-f(a)));
     e1:=(x1+x2)/2;
      while  abs(e1-x1)>e do
        begin
         a:=x1;
         b:=x2;
         x1:= a-f(a)/f1(a);
         x2:= a-((b-a)*f(a)/(f(b)-f(a)));
         e1:=(x1+x2)/2;
         inc(k);
         writeln(k,'    ',x1:10:8);
        end;
writeln ( 'x=',x1:10:8);