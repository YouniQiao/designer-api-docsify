# MediaQuery

提供根据不同媒体类型定义不同的样式。 定义MediaQuery接口。

**起始版本：** 3

**ArkTS模式：** ArkTS-Dyn起始版本为3；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
import { SystemMediaQuery, MediaQueryEvent, MediaQueryList } from '@kit.ArkUI';
```

## matchMedia

```TypeScript
static matchMedia(condition: string): MediaQueryList
```

根据媒体查询条件，创建MediaQueryList对象。

**起始版本：** 3

**ArkTS模式：** ArkTS-Dyn起始版本为3；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| condition | string | 是 |

**返回值：**

| 类型 |
| --- |
| [MediaQueryList](arkts-arkui-system-mediaquery-mediaquerylist-i.md) |

**示例**

```TypeScript
let mMediaQueryList = mediaquery.matchMedia('(max-width: 466)');
```
