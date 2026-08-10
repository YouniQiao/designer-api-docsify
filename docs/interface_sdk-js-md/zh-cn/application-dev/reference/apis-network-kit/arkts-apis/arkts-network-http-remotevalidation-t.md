# RemoteValidation

```TypeScript
export type RemoteValidation = 'system' | 'skip' | ValidationCallback
```

Remote Validation Type.

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-http-export type RemoteValidation = 'system' | 'skip' | ValidationCallback--><!--Device-http-export type RemoteValidation = 'system' | 'skip' | ValidationCallback-End-->

**系统能力：** SystemCapability.Communication.NetStack

| 类型 | 说明 |
| --- | --- |
| 'system' | use system validation. |
| 'skip' | skip validation. |
| ValidationCallback | [since 26.0.0] use custom validation. |

