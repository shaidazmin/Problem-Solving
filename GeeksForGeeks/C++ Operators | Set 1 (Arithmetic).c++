//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution {
  public:
    vector<int> cppOperators(int A, int B) {
          int sum=A+B;
          int mul=A*B;
          int sub,div;
          
          if(A>B)
          {
              sub=A-B;
              div=A/B;
          }
          else 
          {
               sub=B-A;
               div=B/A;
          }
    
          return {sum,mul,sub,div};
       
    }
};


int main() {
    int t;
    cin >> t;
    while (t--) {
        int A, B;
        cin >> A >> B;
        Solution ob;
        vector<int> ans = ob.cppOperators(A, B);
        for (int u : ans) cout << u << "\n";
    }
}