class Solution {
public:
    
    bool bobDfs(int src,int par,int time,vector<int>list[],
                map<int,int>&bobPath)
    {
        if(src==0)
            return true;
        for(auto curr:list[src])
        {
            if(curr!=par)
            {
                if(bobDfs(curr,src,time+1,list,bobPath))
                {
                    bobPath[curr]=time;
                    return true;
                }
            }
        }
        return false;
    }
    
    int aliceDfs(int src,int par,int time,vector<int>&amount,
         vector<int>list[],map<int,int>&bobPath)
    {
        int maxProfit=-1e9;
        for(auto curr:list[src])
        {
            if(curr!=par)
            {
                if(bobPath.count(curr)&&time==bobPath[curr])
                {
                    maxProfit=max(maxProfit,aliceDfs(curr,src,time+1
                            ,amount,list,bobPath)+amount[curr]/2);
                }
                else if(bobPath.count(curr)&&time>bobPath[curr])
                {
                    maxProfit=max(maxProfit,aliceDfs(curr,src,time+1
                            ,amount,list,bobPath));
                }
                else
                {
                    maxProfit=max(maxProfit,aliceDfs(curr,src,time+1
                            ,amount,list,bobPath)+amount[curr]);
                }
            }
        }
        return maxProfit==-1e9?0:maxProfit;
    }
    
    int mostProfitablePath(vector<vector<int>>& edges, int bob, vector<int>& amount) {
        int n=edges.size()+1;
        vector<int>list[n];
        for(auto x:edges)
        {
            list[x[0]].push_back(x[1]);
            list[x[1]].push_back(x[0]);
        }
        map<int,int>bobPath;
        bobPath[bob]=0;
        bobDfs(bob,-1,1,list,bobPath);
        return amount[0]+
            aliceDfs(0,-1,1,amount,list,bobPath);
    }
};