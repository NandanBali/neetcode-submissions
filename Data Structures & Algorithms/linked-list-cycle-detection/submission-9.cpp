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
    bool hasCycle(ListNode* head) {
        ListNode* fp = head;
        ListNode* sp = head;

        if (head != nullptr && head->next == head) return true;

        while (sp != nullptr && fp != nullptr) {
            if (fp < sp) {
                return true;
            } 

            if (sp->next == nullptr || fp->next == nullptr) {
                break;
            } 

            sp = sp->next;
            fp = fp->next->next;
        }
        return false;
    }
};
