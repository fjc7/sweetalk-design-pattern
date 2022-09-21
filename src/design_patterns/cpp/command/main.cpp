//
// Created by HRF on 2022/9/21.
//
#include "OrderCommand.h"

int main() {
    // 开店前的准备
    Barbecuer *boy = new Barbecuer();
    BakeMuttonCommand bakeMuttonCommand1(*boy);
    BakeMuttonCommand bakeMuttonCommand2(*boy);
    BakeChickenWingCommand bakeChickenWingCommand1(*boy);
    Waiter *girl = new Waiter();

    // 开门营业，顾客点菜
    girl->SetOrder(bakeMuttonCommand1);
    girl->SetOrder(bakeMuttonCommand2);
    girl->SetOrder(bakeChickenWingCommand1);

    // 点菜完毕，通知厨房
    girl->Notify();

    return 0;
}
