# TabBarOptions

页签容器数组。

**起始版本：** 12

<!--Device-unnamed-export declare class TabBarOptions--><!--Device-unnamed-export declare class TabBarOptions-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
import { TabBarPosition, TabBarOptions, AtomicServiceTabs, TabContentBuilder, OnContentWillChangeCallback } from '@kit.ArkUI';
```

## constructor

```TypeScript
constructor(icon: ResourceStr | TabBarSymbol, text: ResourceStr,
    unselectedColor?: ResourceColor, selectedColor?: ResourceColor)
```

TabBarOptions的构造函数。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-TabBarOptions-constructor(icon: ResourceStr | TabBarSymbol, text: ResourceStr,    unselectedColor?: ResourceColor, selectedColor?: ResourceColor)--><!--Device-TabBarOptions-constructor(icon: ResourceStr | TabBarSymbol, text: ResourceStr,    unselectedColor?: ResourceColor, selectedColor?: ResourceColor)-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| icon | [ResourceStr](arkts-arkui-resourcestr-t.md) \| TabBarSymbol | 是 | 页签内的图片内容。 |
| text | [ResourceStr](arkts-arkui-resourcestr-t.md) | 是 | 页签内的文字内容。 |
| unselectedColor | [ResourceColor](arkts-arkui-resourcecolor-t.md) | 否 | 未选择时的页签颜色，默认值：#99182431。 |
| selectedColor | [ResourceColor](arkts-arkui-resourcecolor-t.md) | 否 | 被选择时的页签颜色，默认值：#FF007DFF。 |

