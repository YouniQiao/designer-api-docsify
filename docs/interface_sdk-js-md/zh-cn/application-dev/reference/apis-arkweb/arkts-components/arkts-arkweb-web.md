# Web

定义 Web 组件。
<p><strong>API Note</strong>:
<strong>Performance Note</strong>: <p>For details about how to optimize the compilation, resource loading, and JSBridge performance, see Optimizing Web Page Loading <p>When the white screen duration is long due to complex web page parsing, you can enable [optimizeParserBudget](arkts-arkweb-web-attribute.md#optimizeparserbudget) to reduce the first frame rendering content.</p> </p>

## Web

```TypeScript
Web(value: WebOptions)
```

Sets Value.

> **说明：**&gt;
> - 在HTML5侧，调用console.log或console.info对应ConsoleMessage的信息级别都为MessageLevel.Info。

**起始版本：** 8

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebInterface-(value: WebOptions): WebAttribute--><!--Device-WebInterface-(value: WebOptions): WebAttribute-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数:**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [WebOptions](arkts-arkweb-weboptions-i.md) | 是 | Web组件的初始化配置选项，用于设置加载的网页资源（src）、绑定的控制器（controller）以及渲染模式等行为参数。具体属性结构请参考WebOptions接口定义。 |

## 汇总

### 接口

| 名称 | 说明 |
| --- | --- |

### 类型

| 名称 | 说明 |
| --- | --- |

### 枚举

| 名称 | 说明 |
| --- | --- |

