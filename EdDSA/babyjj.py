class Point() :
    def __init__(self, x, y) :
        self.x = x
        self.y = y
 
class Babyjj :
    p = 21888242871839275222246405745257275088548364400416034343698204186575808495617
    n = 21888242871839275222246405745257275088614511777268538073601725287587578984328
    a = 168700
    d = 168696
    l = 2736030358979909402780800718157159386076813972158567259200215660948447373041
    c = 8
    
    G = Point(995203441582195749578291179787384436505546430278305826713579947235728471134,
              5472060717959818805561601436314318772137091100104008585924551046643952123905)
    B = Point(5299619240641551281634865583518297030282874472190772894086521144482721001553,
              16950150798460657717958625567821834550301663161624707787222815936182638968203)
    
    def checkPoint(self, point) :
        x = point.x
        y = point.y
        a = self.a
        d = self.d
        p = self.p
        return 1 if (a * x * x + y * y) % p == (1 + d * x * x * y * y) % p else 0
    
    def pointSum(self, point1, point2) :
        x1 = point1.x
        y1 = point1.y
        x2 = point2.x
        y2 = point2.y
        point3 = Point((x1*y2 + y1*x2) * pow((1 + self.d*x1*x2*y1*y2), -1, self.p) % self.p,
                       (y1*y2 - self.a*x1*x2) * pow((1 - self.d*x1*x2*y1*y2), -1, self.p) % self.p)
        return point3
    
    def scalarMultiplication(self, scalar, point) :
        if scalar == 0 : return self.G
        if scalar == 1 : return point
        if scalar % 2 : return self.pointSum(point, self.scalarMultiplication(scalar - 1, point))
        point2 = self.scalarMultiplication(scalar / 2, point)
        return self.pointSum(point2, point2)


x1 = 17777552123799933955779906779655732241715742912184938656739573121738514868268
y1 = 2626589144620713026669568689430873010625803728049924121243784502389097019475

x2 = 16540640123574156134436876038791482806971768689494387082833631921987005038935
y2 = 20819045374670962167435360035096875258406992893633759881276124905556507972311
point1 = Point(x1, y1)
point2 = Point(x1, y1)
bj = Babyjj()
#print(bj.scalarMultiplication(9, bj.G).x)
#print(bj.pointSum(bj.B, bj.G).x)