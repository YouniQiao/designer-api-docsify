# resetOAID（系统接口）

## resetOAID

```TypeScript
function resetOAID(): void
```

重置开放匿名设备标识符（OAID）。

**起始版本：** 10

<!--Device-identifier-function resetOAID(): void--><!--Device-identifier-function resetOAID(): void-End-->

**系统能力：** SystemCapability.Advertising.OAID

**系统接口：** 此接口为系统接口。

**错误码：**

| 错误码ID |
| --- |
| 17300002 |
| [17300001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ads-kit/errorcode-oaid.md#17300001-系统内部错误) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { identifier } from '@kit.AdsKit';

identifier.resetOAID();
```
