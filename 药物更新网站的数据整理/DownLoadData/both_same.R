a<-read.delim('output_v2.txt',header=F,stringsAsFactors=FALSE,sep='\t')

b<-read.delim('new_data_11_20_wangaodi_v2.txt',header=F,stringsAsFactors=FALSE,sep='')
b_list<-c(1:length(b[,1]))
for(i in c(1:length(b[,1]))){
	if(b[i,2]=='主动暂停'){
		b_list[i]<-'主动暂停'
	}else if(b[i,2]=='已完成'){
		b_list[i]<-'已完成'
	}else if(b[i,2]=='未知'){
		b_list[i]<-'未知'
	}else{
		b_list[i]<-'进行中'
	}

}
b$new_name<-b_list
colnames(b)<-c('sample','state_old','state_old_other')
colnames(a)<-c('sample','state_new','name','des1')
f<-merge(a,b,x.by='sample',y.by='sample')

library(data.table)
d<-fread('output_v1.txt',header=F)
d_new<-as.data.frame(d)
colnames(d_new)<-c('sample','state_new','name','des1','des2')
g<-merge(d_new,b,x.by='sample',y.by='sample')

g_output<-g[-which(g[,2]==g[,7]),]
print(dim(g_output))

write.table(g_output,'without_data.txt',sep='\t',quote=F,row.names=F,col.names=F)
sample_without_put_name<-b[-which(b[,1]%in%g[,1]),1]
print(sample_without_put_name)

