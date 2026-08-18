# shareForm（系统接口）

## 导入模块

```TypeScript
```

## shareForm

```TypeScript
function shareForm(formId: string, deviceId: string, callback: AsyncCallback<void>): void
```

指定formId和远程设备Id进行卡片分享。使用callback异步回调。

**起始版本：** 23

**需要权限：** ohos.permission.REQUIRE_FORM and ohos.permission.DISTRIBUTED_DATASYNC

<!--Device-formHost-function shareForm(formId: string, deviceId: string, callback: AsyncCallback<void>): void--><!--Device-formHost-function shareForm(formId: string, deviceId: string, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| formId | string | 是 |
| deviceId | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [16501003](../errorcode-form.md#16501003-无法操作指定卡片) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16501001](../errorcode-form.md#16501001-卡片id不存在) |
| [16501000](../errorcode-form.md#16501000-内部功能错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [16500050](../errorcode-form.md#16500050-进程间通信失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |


## shareForm

```TypeScript
function shareForm(formId: string, deviceId: string): Promise<void>
```

指定formId和远程设备Id进行卡片分享。使用Promise异步回调。

**起始版本：** 23

**需要权限：** ohos.permission.REQUIRE_FORM and ohos.permission.DISTRIBUTED_DATASYNC

<!--Device-formHost-function shareForm(formId: string, deviceId: string): Promise<void>--><!--Device-formHost-function shareForm(formId: string, deviceId: string): Promise<void>-End-->

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| formId | string | 是 |
| deviceId | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [16501003](../errorcode-form.md#16501003-无法操作指定卡片) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16501001](../errorcode-form.md#16501001-卡片id不存在) |
| [16501000](../errorcode-form.md#16501000-内部功能错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [16500050](../errorcode-form.md#16500050-进程间通信失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
