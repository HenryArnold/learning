Program ex_first;
Users graph;
Var Gm, Gd, R :integer;
Begin
  Gd:=0;
  Write('Please enter the radius:');readln(R);
  Initgraph(Gm, Gd, ' ');
  Setcolor(Green);
  Circle(320, 240, R);
  Readln;
  Closegraph;
End.
