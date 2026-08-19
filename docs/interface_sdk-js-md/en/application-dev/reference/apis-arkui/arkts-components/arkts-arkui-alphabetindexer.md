# AlphabetIndexer

The **AlphabetIndexer** component can create a logically indexed array of items in a container for instant location. > **NOTE**

## Child Components Not supported

## AlphabetIndexer

```TypeScript
AlphabetIndexer(options: AlphabetIndexerOptions)
```

Creates an **AlphabetIndexer** component.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AlphabetIndexerInterface-(options: AlphabetIndexerOptions): AlphabetIndexerAttribute--><!--Device-AlphabetIndexerInterface-(options: AlphabetIndexerOptions): AlphabetIndexerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [AlphabetIndexerOptions](arkts-arkui-alphabetindexeroptions-i.md) | Yes | Options of the **AlphabetIndexer** component. |

## Summary

### Interfaces

| Name | Description |
| --- | --- |
| [AlphabetIndexerOptions](arkts-arkui-alphabetindexeroptions-i.md) | Defines the options of the **AlphabetIndexer** component. &gt; **NOTE：**&gt; To standardize anonymous object definitions, the element definitions here have been revised in API version 18. &gt; While historical version information is preserved for anonymous objects, there may be cases where the outer element &gt; 's @since version number is higher than inner elements'. This does not affect interface usability. |

### Types

| Name | Description |
| --- | --- |
| [OnAlphabetIndexerPopupSelectCallback](arkts-arkui-onalphabetindexerpopupselectcallback-t.md) | Represents the callback invoked when a secondary index item in the pop-up window is selected. |
| [OnAlphabetIndexerRequestPopupDataCallback](arkts-arkui-onalphabetindexerrequestpopupdatacallback-t.md) | Represents the callback invoked when an index item is selected and [usingPopup](arkts-arkui-alphabetindexer-attribute.md#usingpopup) is set to **true**. |
| [OnAlphabetIndexerSelectCallback](arkts-arkui-onalphabetindexerselectcallback-t.md) | Represents the callback invoked when an index item is selected. |

### Enums

| Name | Description |
| --- | --- |
| [IndexerAlign](arkts-arkui-indexeralign-e.md) | Enumerates the alignment styles of the indexer pop-up window. |

