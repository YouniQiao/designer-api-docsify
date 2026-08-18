# onEnabledAccessibilityExtensionListChange（系统接口）

## 导入模块

```TypeScript
```

## onEnabledAccessibilityExtensionListChange

```TypeScript
function onEnabledAccessibilityExtensionListChange(callback: Callback<void>): void
```

Register the listener that watches for changes in the enabled status of accessibility extensions.

**起始版本：** 23

**需要权限：** ohos.permission.READ_ACCESSIBILITY_CONFIG

<!--Device-config-function onEnabledAccessibilityExtensionListChange(callback: Callback<void>): void--><!--Device-config-function onEnabledAccessibilityExtensionListChange(callback: Callback<void>): void-End-->

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
