# getTimeZone

## 导入模块

```TypeScript
import { i18n } from 'kits/@kit.LocalizationKit';
```

## getTimeZone

```TypeScript
export function getTimeZone(zoneID?: string): TimeZone
```

获取时区ID对应的时区对象。

**起始版本：** 7

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| zoneID | string | 否 |

**返回值：**

| 类型 |
| --- |
| [TimeZone](arkts-localization-i18n-timezone-c.md) |
