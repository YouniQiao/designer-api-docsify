# begin（系统接口）

## 导入模块

```TypeScript
import { performanceMonitor } from 'kits/@kit.ArkUI';
```

## begin

```TypeScript
function begin(scene: string, startInputType: ActionType, note?: string): void
```

用于标记用户场景开始，用户场景开始时调用此接口。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| scene | string | 是 |
| startInputType | [ActionType](../../apis-data-protection-kit/arkts-apis/arkts-dataprotection-dlppermission-actiontype-e.md) | 是 |
| [note](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-contact-c.md) | string | 否 |
