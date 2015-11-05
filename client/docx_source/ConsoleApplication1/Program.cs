using System;
using System.Collections.Generic;
using System.Text;
using Microsoft.Office.Interop.Word;
using Microsoft.Office.Core;

namespace docx_comp
{
    class Program
    {
        static void Main(string[] args)
        {            
            Application wordApp = new Application();
            wordApp.Visible = false;
            wordApp.DisplayAlerts = WdAlertLevel.wdAlertsNone;
            object wordTrue = (object)true;
            object wordFalse = (object)false;
            object fileToOpen = args[0];
            object missing = Type.Missing;            
            Document doc1 = wordApp.Documents.Open(ref fileToOpen,
               ref missing, ref wordFalse, ref wordTrue, ref missing,
               ref missing, ref missing, ref missing, ref missing,
               ref missing, ref missing, ref wordTrue, ref missing,
               ref missing, ref missing, ref missing);
            
            object fileToOpen1 = args[1];
            Document doc2 = wordApp.Documents.Open(ref fileToOpen1,
                ref missing, ref wordFalse, ref wordTrue, ref missing,
                ref missing, ref missing, ref missing, ref missing,
                ref missing, ref missing, ref missing, ref missing,
                ref missing, ref missing, ref missing);

            Document doc = wordApp.CompareDocuments(doc1, doc2, WdCompareDestination.wdCompareDestinationNew, WdGranularity.wdGranularityWordLevel,
                true, true, true, true, true, true, true, true, true, true, "", false);

            object resultFile = args[2];
            object resultType = WdSaveFormat.wdFormatXMLDocument;
            doc.SaveAs(ref resultFile, ref resultType, ref missing, ref missing, ref missing, ref missing, ref missing, 
                ref missing, ref missing, ref missing, ref missing, ref missing, ref missing, ref missing, ref missing, ref missing);
            ((_Application)wordApp).Quit(ref missing, ref missing, ref missing);
        }
    }
}
