/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    void reorderList(ListNode* head) {
        ListNode* r = head;
        vector<ListNode> st;
        while (r != nullptr) {
            ListNode x = *r;
            x.next = nullptr;
            st.push_back(x);
            r = r->next;
        }

        for (auto& x : st) {
            cout << x.val << " ";
        }
        cout << endl;
        
        int len = st.size();

        ListNode* it = head;
        auto ac = new ListNode();
        auto res = ac;
        while (st.size() > (len/2)) {
            ac->next = it;
            it = it->next;
            ac = ac->next;
            ListNode* n = new ListNode(st.back().val);
            if (len % 2 == 1 && st.size() - (len/2) == 1) {
                ac->next = nullptr;
            } else {
                ac->next = n;
                ac = ac->next;
            }
            st.pop_back();
        }
        head = res->next;
    }
};
