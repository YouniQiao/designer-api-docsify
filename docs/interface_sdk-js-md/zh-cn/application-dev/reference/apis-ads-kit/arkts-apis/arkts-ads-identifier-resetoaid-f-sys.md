# resetOAID（系统接口）

## 导入模块

```TypeScript
import { identifier } from '@kit.AdsKit';
```

## resetOAID

```TypeScript
function resetOAID(): void
```

重置开放匿名设备标识符（OAID）。

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为10。

**系统能力：** SystemCapability.Advertising.OAID

**系统接口：** 此接口为系统接口。

**错误码：**

| 错误码ID |
| --- |
| [17300001](../errorcode-oaid.md#17300001-系统内部错误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| 17300002 |

**示例**

```TypeScript
import { identifier } from '@kit.AdsKit';

identifier.resetOAID();
```
