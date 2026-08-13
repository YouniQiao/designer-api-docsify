# create

## create

```TypeScript
function create(colorSpaceName: ColorSpace): ColorSpaceManager
```

创建标准色域对象。

**起始版本：** 23

**废弃版本：** -1

<!--Device-colorSpaceManager-function create(colorSpaceName: ColorSpace): ColorSpaceManager--><!--Device-colorSpaceManager-function create(colorSpaceName: ColorSpace): ColorSpaceManager-End-->

**系统能力：** SystemCapability.Graphic.Graphic2D.ColorManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| colorSpaceName | [ColorSpace](../../apis-arkui/arkts-apis/arkts-arkui-window-colorspace-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [ColorSpaceManager](arkts-arkgraphics2d-sendablecolorspacemanager-colorspacemanager-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [18600001](../errorcode-colorspace-manager.md#18600001-参数值异常) |

## 示例

```TypeScript
try {
  // 创建标准SRGB色域的色彩管理实例
  let colorSpace = colorSpaceManager.create(colorSpaceManager.ColorSpace.SRGB);
} catch (err) {
  console.error(`Failed to create SRGB colorSpace. Code: ${err.code}, message: ${err.message}`);
}
```


## create

```TypeScript
function create(primaries: ColorSpacePrimaries, gamma: number): ColorSpaceManager
```

创建用户自定义色域对象。

**起始版本：** 23

**废弃版本：** -1

<!--Device-colorSpaceManager-function create(primaries: ColorSpacePrimaries, gamma: double): ColorSpaceManager--><!--Device-colorSpaceManager-function create(primaries: ColorSpacePrimaries, gamma: double): ColorSpaceManager-End-->

**系统能力：** SystemCapability.Graphic.Graphic2D.ColorManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| primaries | [ColorSpacePrimaries](arkts-arkgraphics2d-colorspacemanager-colorspaceprimaries-i.md) | 是 |
| gamma | number | 是 |

**返回值：**

| 类型 |
| --- |
| [ColorSpaceManager](arkts-arkgraphics2d-sendablecolorspacemanager-colorspacemanager-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [18600001](../errorcode-colorspace-manager.md#18600001-参数值异常) |

## 示例

```TypeScript
try {
  // 定义色域标准三原色参数
  let primaries: colorSpaceManager.ColorSpacePrimaries = {
    redX: 0.1,
    redY: 0.1,
    greenX: 0.2,
    greenY: 0.2,
    blueX: 0.3,
    blueY: 0.3,
    whitePointX: 0.4,
    whitePointY: 0.4
  };
  // 定义色域gamma值
  let gamma = 2.2;
  // 创建自定义色域对象
  let colorSpace = colorSpaceManager.create(primaries, gamma);
} catch (err) {
  console.error(`Failed to create colorSpace with customized primaries and gamma. Code: ${err.code}, message: ${err.message}`);
}
```
