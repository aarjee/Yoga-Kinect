joints = read.csv('joints.csv', header = F)
joints$V3 = as.factor(joints$V3)
typeof(joints$V3)
spinebase = joints[which(joints$V3 == 'JointType_SpineBase'),]
n = 100
x = spinebase$V8
y = spinebase$V9
z = spinebase$V10
length(x)
vrx = c()
vry = c()
vrz = c()

ts = as.character(spinebase$V2) 
newTs = strsplit(ts,':')
matty = matrix(unlist(newTs), ncol = 3, byrow = T)
timeS = as.numeric(matty[,3])
timeS1 = as.numeric(matty[,2])
timeS2 = as.numeric(matty[,1])

mx = mean(x)
my = mean(y)
mz = mean(z)
sumx = c()
sumy = c()
sumz = c()
frameRateInv = c(0)

varX = c()
varY = c()
varZ = c()

#for (i in c(1:n)) {
 # p1 = as.integer((i-1)*length(x)/n) + 1
 #p2 = as.integer(i*length(x)/n) + 1
#  varX = c(varX, var(x[p1:p2]))
 # varY = c(varY, var(y[p1:p2]))
#  varZ = c(varZ, var(z[p1:p2]))
#}

for (i in c(2:length(x))){
  frameRateInv = c(frameRateInv,(timeS[i]-timeS[i-1]) + 60*(timeS1[i]-timeS1[i-1]) + 3600*(timeS2[i]-timeS2[i-1]))
  sumx = c(sumx, frameRateInv[i]*((x[i]-mx)^2))
  sumy = c(sumy, frameRateInv[i]*((y[i]-my)^2))
  sumz = c(sumz, frameRateInv[i]*((z[i]-mz)^2))
}

normalizer = (sum(frameRateInv**2))**(1/2)
#normalizedSums
NSx = (sum(sumx)/normalizer)**(1/2)
NSy = (sum(sumy)/normalizer)**(1/2)
NSz = (sum(sumz)/normalizer)**(1/2)

plot(sumx)
plot(sumy)
plot(sumz)
