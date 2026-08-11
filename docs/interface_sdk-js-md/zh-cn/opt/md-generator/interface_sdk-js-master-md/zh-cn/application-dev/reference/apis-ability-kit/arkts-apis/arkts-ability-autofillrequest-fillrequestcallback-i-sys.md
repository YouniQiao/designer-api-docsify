# FillRequestCallback（系统接口）

自动填充或者生成密码时的回调对象，可以通过此回调通知客户端成功或者失败。

**起始版本：** 11

<!--Device-unnamed-export interface FillRequestCallback--><!--Device-unnamed-export interface FillRequestCallback-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**系统接口：** 此接口为系统接口。

## onCancel

```TypeScript
onCancel(fillContent?: string): void
```

通知自动填充已被取消。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FillRequestCallback-onCancel(fillContent?: string): void--><!--Device-FillRequestCallback-onCancel(fillContent?: string): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| fillContent | string | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## onFailure

```TypeScript
onFailure(): void
```

通知自动填充请求已失败。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FillRequestCallback-onFailure(): void--><!--Device-FillRequestCallback-onFailure(): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**系统接口：** 此接口为系统接口。

**错误码：**

| 错误码ID |
| --- |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## onSuccess

```TypeScript
onSuccess(response: FillResponse): void
```

通知自动填充请求已成功完成。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FillRequestCallback-onSuccess(response: FillResponse): void--><!--Device-FillRequestCallback-onSuccess(response: FillResponse): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| response | [FillResponse](arkts-ability-autofillrequest-fillresponse-i-sys.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## setAutoFillPopupConfig

```TypeScript
setAutoFillPopupConfig(autoFillPopupConfig: AutoFillPopupConfig): void
```

动态调整气泡弹窗的尺寸和位置。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FillRequestCallback-setAutoFillPopupConfig(autoFillPopupConfig: AutoFillPopupConfig): void--><!--Device-FillRequestCallback-setAutoFillPopupConfig(autoFillPopupConfig: AutoFillPopupConfig): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| autoFillPopupConfig | [AutoFillPopupConfig](arkts-ability-autofillpopupconfig-i-sys.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
