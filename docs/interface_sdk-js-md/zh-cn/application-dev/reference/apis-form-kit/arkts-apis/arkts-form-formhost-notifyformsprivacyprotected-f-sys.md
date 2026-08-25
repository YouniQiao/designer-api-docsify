# notifyFormsPrivacyProtected（系统接口）

## 导入模块

```TypeScript
import { formHost } from 'kits/@kit.FormKit';
```

## notifyFormsPrivacyProtected

```TypeScript
function notifyFormsPrivacyProtected(
    formIds: Array<string>,
    isProtected: boolean,
    callback: AsyncCallback<void>
  ): void
```

通知指定卡片隐私保护状态改变。使用callback异步回调。

**起始版本：** 9

**需要权限：** ohos.permission.REQUIRE_FORM

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| formIds | Array & lt;string & gt; | 是 |
| isProtected | boolean | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16500050](../errorcode-form.md#16500050-进程间通信失败) |
| [16500060](../errorcode-form.md#16500060-连接服务失败) |
| [16501000](../errorcode-form.md#16501000-内部功能错误) |


## notifyFormsPrivacyProtected

```TypeScript
function notifyFormsPrivacyProtected(formIds: Array<string>, isProtected: boolean): Promise<void>
```

通知指定卡片隐私保护状态改变。使用Promise异步回调。

**起始版本：** 9

**需要权限：** ohos.permission.REQUIRE_FORM

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| formIds | Array & lt;string & gt; | 是 |
| isProtected | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16500050](../errorcode-form.md#16500050-进程间通信失败) |
| [16500060](../errorcode-form.md#16500060-连接服务失败) |
| [16501000](../errorcode-form.md#16501000-内部功能错误) |
