#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

struct Point {
    double x, y;
};

Point bezier(Point P0, Point P1, Point P2, Point P3, double t)
{
    double u = 1.0 - t;

    double b0 = u*u*u;
    double b1 = 3*u*u*t;
    double b2 = 3*u*t*t;
    double b3 = t*t*t;

    Point B;

    B.x = b0*P0.x + b1*P1.x + b2*P2.x + b3*P3.x;
    B.y = b0*P0.y + b1*P1.y + b2*P2.y + b3*P3.y;

    return B;
}

double dist(Point a, Point b)
{
    return sqrt((a.x-b.x)*(a.x-b.x)
              + (a.y-b.y)*(a.y-b.y));
}

double curveLength(Point P0, Point P1,
                   Point P2, Point P3)
{
    int N = 100;

    double L = 0.0;

    Point prev = bezier(P0,P1,P2,P3,0);

    for(int i=1;i<=N;i++)
    {
        double t = (double)i/N;

        Point curr = bezier(P0,P1,P2,P3,t);

        L += dist(prev,curr);

        prev = curr;
    }

    return L;
}

bool insideRock(Point p)
{
    double dx = p.x - 4.0;
    double dy = p.y - 3.0;

    return dx*dx + dy*dy < 1.2*1.2;
}

bool insideHouse(Point p)
{
    return (p.x >= 6 &&
            p.x <= 8 &&
            p.y >= 1 &&
            p.y <= 4);
}

bool validCurve(Point P0, Point P1,
                Point P2, Point P3)
{
    int N = 300;

    for(int i=0;i<=N;i++)
    {
        double t = (double)i/N;

        Point p = bezier(P0,P1,P2,P3,t);

        if(insideRock(p))
            return false;

        if(insideHouse(p))
            return false;
    }

    return true;
}

int main()
{
    Point P0 = {0,0};
    Point P3 = {10,5};

    double bestLen = 1e18;

    Point bestP1, bestP2;

    for(double x1=0;x1<=10;x1+=0.1)
    {
        for(double y1=0;y1<=7;y1+=0.1)
        {
            for(double x2=0;x2<=10;x2+=0.1)
            {
                for(double y2=0;y2<=7;y2+=0.1)
                {
                    Point P1 = {x1,y1};
                    Point P2 = {x2,y2};

                    if(validCurve(P0,P1,P2,P3))
                    {
                        double L =
                        curveLength(P0,P1,P2,P3);

                        if(L < bestLen)
                        {
                            bestLen = L;

                            bestP1 = P1;
                            bestP2 = P2;
                        }
                    }
                }
            }
        }
    }

    cout << "Mejor longitud: "
         << bestLen << endl;

    cout << "P1 = ("
         << bestP1.x << ", "
         << bestP1.y << ")\n";

    cout << "P2 = ("
         << bestP2.x << ", "
         << bestP2.y << ")\n";
}