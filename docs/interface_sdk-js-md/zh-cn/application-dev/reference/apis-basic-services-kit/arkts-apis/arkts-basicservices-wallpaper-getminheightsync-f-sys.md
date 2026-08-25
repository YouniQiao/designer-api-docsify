# getMinHeightSync（系统接口）

## 导入模块

```TypeScript
import { wallpaper } from '@kit.BasicServicesKit';
```

## getMinHeightSync

```TypeScript
function getMinHeightSync(): int
```

获取壁纸的最小高度值。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.Wallpaper

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| ArkTS-Dyn: number<br>ArkTS-Sta：int |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
    let minHeight = wallpaper.getMinHeightSync();
    console.info(`success to getMinHeightSync: ${JSON.stringify(minHeight)}`);
} catch (error) {
    let err = error as BusinessError;
    console.error(`Failed to getMinHeightSync. Code: ${err.code}, message: ${err.message}`);
}
```
