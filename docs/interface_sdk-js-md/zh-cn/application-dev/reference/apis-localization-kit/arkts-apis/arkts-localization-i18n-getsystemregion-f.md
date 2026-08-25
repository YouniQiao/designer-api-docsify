# getSystemRegion

## 导入模块

```TypeScript
import { i18n } from '@kit.LocalizationKit';
```

## getSystemRegion

```TypeScript
export function getSystemRegion(): string
```

获取系统地区。

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为7。

**废弃版本：** 9

**替代接口：** [getSystemRegion](arkts-localization-i18n-system-c.md#getsystemregion)

**系统能力：** SystemCapability.Global.I18n

**返回值：**

| 类型 |
| --- |
| string |

**示例**

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let systemRegion: string = i18n.System.getSystemRegion(); // 如果系统地区为中国，systemRegion = 'CN'
```

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let region: string = i18n.getSystemRegion();
```
