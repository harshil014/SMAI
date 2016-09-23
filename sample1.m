load 'data.mat'
count =zeros(size(set,2),1);
for i=1:size(set,2)
    for j=1:size(set,1)
        if(set(j,i)==-1)
            count(i)=count(i)+1;
        end
    end
end
i=1:size(set,2)
extract=find(count>100);
insert=setdiff(i,extract);
for i=1:size(insert,2)
    mean1(i)=mean(set(:,insert(i)))
end
for i=1:size(insert,2)
    std1(i)=std(set(:,insert(i)))
end

for i=1:size(insert,2)
    Y(:,i)=(set(:,insert(i))-mean1(i))/(std1(i).^2);
end

[a,b]=pca(Y);
a=a(1:3,:);
size(a);
dat=b*a';
S=kmeans(dat,15);

