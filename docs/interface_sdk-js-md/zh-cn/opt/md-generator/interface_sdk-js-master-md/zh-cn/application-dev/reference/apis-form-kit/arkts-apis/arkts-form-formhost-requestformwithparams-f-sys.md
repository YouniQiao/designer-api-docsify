# requestFormWithParams（系统接口）

## 导入模块

```TypeScript
```

## requestFormWithParams

```TypeScript
function requestFormWithParams(formId: string, wantParams?: Record<string, Object>): Promise<void>
```

携带参数请求卡片更新。使用Promise异步回调。

**起始版本：** 23

**需要权限：** ohos.permission.REQUIRE_FORM

<!--Device-formHost-function requestFormWithParams(formId: string, wantParams?: Record<string, Object>): Promise<void>--><!--Device-formHost-function requestFormWithParams(formId: string, wantParams?: Record<string, Object>): Promise<void>-End-->

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| formId | string | 是 |
| wantParams | Record & lt;string, Object & gt; | 否 |

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
| [16500060](../errorcode-form.md#16500060-连接服务失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [16500050](../errorcode-form.md#16500050-进程间通信失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
