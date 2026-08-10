# AddFormMenuItem

## 导入模块

```TypeScript
import { AddFormMenuItem, AddFormOptions, FormMenuItemStyle } from 'kits/@kit.ArkUI';
```

## AddFormMenuItem

```TypeScript
export declare function AddFormMenuItem(
  want: Want,
  componentId: string,
  options?: AddFormOptions
): void
```

Build function of AddFormMenuItem.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**装饰器类型：** @Builder

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-unnamed-export declare function AddFormMenuItem(  want: Want,  componentId: string,  options?: AddFormOptions): void--><!--Device-unnamed-export declare function AddFormMenuItem(  want: Want,  componentId: string,  options?: AddFormOptions): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 | The want of the form to publish. |
| componentId | string | 是 | The id of the component used to get form snapshot. |
| options | [AddFormOptions](arkts-arkui-arkui-advanced-formmenu-addformoptions-i.md) | 否 | Add form options. |

