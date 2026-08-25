# PrintExtensionAbility

该模块提供打印扩展能力的调用接口。PrintExtensionAbility基于生命周期回调机制运行，系统在打印扩展连接、发现打印机、连接/断开打印机、查询打印机能力、启动/取消打印任务等场景下分别调用相应回调方法，开发者需在各回调中 实现对应的打印扩展逻辑。

**起始版本：** 14

**系统能力：** SystemCapability.Print.PrintFramework

## 导入模块

```TypeScript
import { PrintExtensionAbility } from 'kits/@kit.BasicServicesKit';
```

## onCancelPrintJob

```TypeScript
public onCancelPrintJob(jobInfo: print.PrintJob): void
```

取消已开始的打印任务时调用。开发者应在此回调中实现取消打印任务的逻辑，停止正在进行的打印操作并清理相关资源。

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| jobInfo | print.PrintJob | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## onConnectPrinter

```TypeScript
onConnectPrinter(printerId: number): void
```

连接到特定打印机时调用。开发者应在此回调中实现与指定打印机（通过printerId标识）的连接逻辑。

**起始版本：** 14

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| printerId | number | 是 |

## onCreate

```TypeScript
onCreate(want: Want): void
```

系统首次连接打印扩展能力时调用。开发者可在此回调中完成打印扩展能力的初始化工作，如初始化必要的资源、状态等。

**起始版本：** 14

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |

## onDestroy

```TypeScript
onDestroy(): void
```

结束打印扩展能力时调用。开发者应在此回调中释放相关资源并完成必要的清理工作。

**起始版本：** 14

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Print.PrintFramework

## onDisconnectPrinter

```TypeScript
onDisconnectPrinter(printerId: number): void
```

断开与特定打印机的连接时调用。开发者应在此回调中实现断开打印机连接的逻辑并释放相关资源。

**起始版本：** 14

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| printerId | number | 是 |

## onRequestPrinterCapability

```TypeScript
public onRequestPrinterCapability(printerId: number): print.PrinterCapability
```

请求打印机支持的能力特性（如色彩模式、双面打印模式、纸张尺寸等）时调用，例如在打印设置界面中用户选择打印机后，系统需要获取该打印机支持的能力信息时触发此回调。 开发者应在此回调中根据printerId查询并返回对应打印机的能力信息（print.PrinterCapability）。

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| printerId | number | 是 |

**返回值：**

| 类型 |
| --- |
| print.PrinterCapability |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## onStartDiscoverPrinter

```TypeScript
onStartDiscoverPrinter(): void
```

开始发现打印机时调用。开发者可在此回调中实现自己的打印机发现逻辑，可通过 [addPrinterToDiscovery](arkts-basicservices-print-addprintertodiscovery-f.md) 将发现的打印机 信息上报给系统。

**起始版本：** 14

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Print.PrintFramework

## onStartPrintJob

```TypeScript
public onStartPrintJob(jobInfo: print.PrintJob): void
```

开始打印任务时调用。开发者应在此回调中根据jobInfo中的任务信息处理打印操作，如解析打印任务参数并执行相应的打印流程。

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| jobInfo | print.PrintJob | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## onStopDiscoverPrinter

```TypeScript
onStopDiscoverPrinter(): void
```

停止发现打印机时调用。开发者应在此回调中停止打印机发现流程并释放相关资源。

**起始版本：** 14

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Print.PrintFramework

## context

```TypeScript
context: PrintExtensionContext
```

打印扩展能力上下文。

**类型：** [PrintExtensionContext](arkts-basicservices-printextensioncontext-c.md)

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Print.PrintFramework
