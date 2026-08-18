# recycleForms（系统接口）

## 导入模块

```TypeScript
```

## recycleForms

```TypeScript
function recycleForms(formIds: Array<string>): Promise<void>
```

立即回收卡片内存。使用Promise异步回调。

**起始版本：** 23

**需要权限：** ohos.permission.REQUIRE_FORM

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-formHost-function recycleForms(formIds: Array<string>): Promise<void>--><!--Device-formHost-function recycleForms(formIds: Array<string>): Promise<void>-End-->

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| formIds | Array & lt;string & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16501000](../errorcode-form.md#16501000-内部功能错误) |
| [16500060](../errorcode-form.md#16500060-连接服务失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [16500050](../errorcode-form.md#16500050-进程间通信失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
