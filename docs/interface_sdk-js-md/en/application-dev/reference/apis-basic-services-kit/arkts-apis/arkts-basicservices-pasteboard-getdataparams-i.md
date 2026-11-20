# GetDataParams

```TypeScript
interface GetDataParams
```

Obtains parameters when an application uses the file copy capability provided by the pasteboard, including the destination path, file conflict options, and progress indicator types. Before calling this API, ensure that no other copy or paste operation is in progress.

**Since:** 15

<!--Device-pasteboard-interface GetDataParams--><!--Device-pasteboard-interface GetDataParams-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

## Modules to Import

```TypeScript
import { pasteboard } from '@kit.BasicServicesKit';
```

## progressListener

```TypeScript
progressListener?: ProgressListener
```

Listener for progress data changes, which is used to obtain the pasting progress. This parameter is valid only when **progressIndicator** is set to **NONE**. When **progressIndicator** is set to **DEFAULT**, this parameter is invalid. By default, this parameter is left empty (the progress is not listened to).

**Since:** 15

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-GetDataParams-progressListener?: ProgressListener--><!--Device-GetDataParams-progressListener?: ProgressListener-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

## destUri

```TypeScript
destUri?: string
```

URI of the destination directory for the file copied. If file processing is not supported, this parameter is not required. If the application involves complex file processing policies or needs to distinguish file multipathing storage, you are advised not to set this parameter but let the application copy files by itself. This parameter is left empty by default.

**Type:** string

**Default:** -

**Since:** 15

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-GetDataParams-destUri?: string--><!--Device-GetDataParams-destUri?: string-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

## fileConflictOptions

```TypeScript
fileConflictOptions?: FileConflictOptions
```

Options used to resolve file copy conflicts. Set this parameter to **OVERWRITE** when the latest file content must be used in the destination URI. Set this parameter to **SKIP** when the original file in the destination URI needs to be retained to prevent accidental overwriting. The default value is **OVERWRITE**.

**Type:** [FileConflictOptions](arkts-basicservices-pasteboard-fileconflictoptions-e.md)

**Default:** FileConflictOptions.OVERWRITE

**Since:** 15

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-GetDataParams-fileConflictOptions?: FileConflictOptions--><!--Device-GetDataParams-fileConflictOptions?: FileConflictOptions-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

## progressIndicator

```TypeScript
progressIndicator: ProgressIndicator
```

Progress indicator options. You can use the default progress indicator as required. If this parameter is set to **DEFAULT**, the default system progress indicator is used. If this parameter is set to **NONE**, the app progress indicator is used. Only in the second case, the **progressListener** and **progressSignal** parameters are valid.

**Type:** [ProgressIndicator](arkts-basicservices-pasteboard-progressindicator-e.md)

**Since:** 15

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-GetDataParams-progressIndicator: ProgressIndicator--><!--Device-GetDataParams-progressIndicator: ProgressIndicator-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

## progressSignal

```TypeScript
progressSignal?: ProgressSignal
```

Function for canceling the paste task. This parameter is valid only when [ProgressIndicator](arkts-basicservices-pasteboard-progressindicator-e.md) is set to **NONE**. This parameter is left empty by default.

**Type:** [ProgressSignal](arkts-basicservices-pasteboard-progresssignal-c.md)

**Default:** -

**Since:** 15

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-GetDataParams-progressSignal?: ProgressSignal--><!--Device-GetDataParams-progressSignal?: ProgressSignal-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard
