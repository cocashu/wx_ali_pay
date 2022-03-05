# 一个文件搞定微信支付宝的付款码

这个开发项目的一个副产品，用于跟Delphi开发的收款项目对比收款时间。
一个文件就能完成微信的扫码支付，就不整那么多目录和框架了。

# 目前完成

[wechat_pay.py](https://github.com/cocashu/wx_ali_pay/blob/main/wechat_pay.py)：一个文件使用微信收款码收款，完整的实现了扫码支付的全部过程，每一步都有说明。
网上也有类似的项目看过php的。反正都写了，就正好学习一下上传GitHub.

## 在做的项目

一个商场的的收款系统，目前的支付中间层仅支持每种支付方式支持一个账户收款，我要做的就是可以多账户分别收款。不是微信支付那种的微信分账。

## 使用方式

> 记得修改里面的配置参数和收款账户等

    python wechat_pay.py
