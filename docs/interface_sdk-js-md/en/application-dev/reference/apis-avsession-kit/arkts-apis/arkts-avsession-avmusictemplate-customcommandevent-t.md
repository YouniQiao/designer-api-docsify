# CustomCommandEvent

```TypeScript
type CustomCommandEvent = (command: string, args: string) => Promise<OperResult>
```

The custom command event.

**Since:** 26.1.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-avMusicTemplate-type CustomCommandEvent = (command: string, args: string) => Promise<OperResult>--><!--Device-avMusicTemplate-type CustomCommandEvent = (command: string, args: string) => Promise<OperResult>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| command | string | Yes | request command.  |
| args | string | Yes | arguments associated with event.  |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;OperResult&gt; | Promise used to return OperResult.  |

