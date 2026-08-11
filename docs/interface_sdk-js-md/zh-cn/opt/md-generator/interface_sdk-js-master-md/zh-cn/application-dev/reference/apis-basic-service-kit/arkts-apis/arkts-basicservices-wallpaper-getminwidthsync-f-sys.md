# getMinWidthSync（系统接口）

## getMinWidthSync

```TypeScript
function getMinWidthSync(): number
```

获取壁纸的最小宽度值。

**起始版本：** 9

<!--Device-wallpaper-function getMinWidthSync(): int--><!--Device-wallpaper-function getMinWidthSync(): int-End-->

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
  let minWidth = wallpaper.getMinWidthSync();
  console.info(`success to getMinWidthSync: ${JSON.stringify(minWidth)}`);
} catch (error) {
  console.error(`failed to getMinWidthSync. Code: ${error.code}, Message: ${error.message}`);
}
```
