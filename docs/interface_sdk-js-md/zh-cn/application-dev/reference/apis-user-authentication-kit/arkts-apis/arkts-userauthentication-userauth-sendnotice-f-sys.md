# sendNotice（系统接口）

## 导入模块

```TypeScript
import { userAuth } from 'kits/@kit.UserAuthenticationKit';
```

## sendNotice

```TypeScript
function sendNotice(noticeType: NoticeType, eventData: string): void
```

发送来自身份认证组件的通知。在使用统一身份认证控件进行用户身份认证时，该接口用于接收来自统一身份认证组件的通知，并将通知发送给用户认证框架。

**起始版本：** 10

**需要权限：** ohos.permission.SUPPORT_USER_AUTH

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| noticeType | [NoticeType](arkts-userauthentication-userauth-noticetype-e-sys.md) | 是 |
| eventData | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12500002](../errorcode-useriam.md#12500002-身份认证系统通用错误码) |
