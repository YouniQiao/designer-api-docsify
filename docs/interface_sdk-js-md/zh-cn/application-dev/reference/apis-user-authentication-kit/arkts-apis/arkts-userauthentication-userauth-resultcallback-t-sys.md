# ResultCallback（系统接口）

```TypeScript
type ResultCallback = (challenge: Uint8Array, result: UserAuthResult) => void
```

返回远程认证结果的回调函数类型。该类型用于远程认证场景，在远程认证完成后，系统会调用此回调函数返回认证结果。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| challenge | Uint8Array | 是 |
| result | [UserAuthResult](../../apis-background-tasks-kit/arkts-apis/arkts-backgroundtasks-backgroundtaskmanager-userauthresult-e.md) | 是 |
