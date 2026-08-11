# getMinHeightSync（系统接口）

## getMinHeightSync

```TypeScript
function getMinHeightSync(): number
```

获取壁纸的最小高度值。

**起始版本：** 9

<!--Device-wallpaper-function getMinHeightSync(): int--><!--Device-wallpaper-function getMinHeightSync(): int-End-->

**系统能力：** SystemCapability.MiscServices.Wallpaper

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
try {
  let minHeight = wallpaper.getMinHeightSync();
  console.info(`success to getMinHeightSync: ${JSON.stringify(minHeight)}`);
} catch (error) {
  console.error(`failed to getMinHeightSync. Code: ${error.code}, Message: ${error.message}`);
}
```
