# begin（系统接口）

## begin

```TypeScript
function begin(scene: string, startInputType: ActionType, note?: string): void
```

用于标记用户场景开始，用户场景开始时调用此接口。

**起始版本：** 10

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-performanceMonitor-function begin(scene: string, startInputType: ActionType, note?: string): void--><!--Device-performanceMonitor-function begin(scene: string, startInputType: ActionType, note?: string): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| scene | string | 是 |
| startInputType | [ActionType](../../apis-avsession-kit/arkts-apis/arkts-avsession-avmusictemplate-actiontype-t.md) | 是 |
| [note](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-contact-c.md) | string | 否 |

## 示例

用户点击图标启动应用场景动效开始点，由离手事件LAST_UP触发。

```TypeScript
performanceMonitor.begin("LAUNCHER_APP_LAUNCH_FROM_ICON", performanceMonitor.ActionType.LAST_UP, "APP_START_BEGIN");
```
