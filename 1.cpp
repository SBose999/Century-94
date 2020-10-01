#include <bits/stdc++.h>

#define int long long

using namespace std;

int n;
string s;

void solve() {
    cin >> n;
    cin >> s;
    for (int i = 0; i < n * 2 - 1; i += 2)
        cout << s[i];
    cout << '\n';
}

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    int t;
    cin >> t;
    while (t--)
        solve();
    return 0;
}
