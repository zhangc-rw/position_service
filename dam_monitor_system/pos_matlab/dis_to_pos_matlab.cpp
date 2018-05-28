//
// MATLAB Compiler: 6.2 (R2016a)
// Date: Fri May 25 17:06:02 2018
// Arguments: "-B" "macro_default" "-W" "cpplib:dis_to_pos_matlab" "-T"
// "link:lib" "dis_to_pos_matlab" 
//

#include <stdio.h>
#define EXPORTING_dis_to_pos_matlab 1
#include "dis_to_pos_matlab.h"

static HMCRINSTANCE _mcr_inst = NULL;


#if defined( _MSC_VER) || defined(__BORLANDC__) || defined(__WATCOMC__) || defined(__LCC__)
#ifdef __LCC__
#undef EXTERN_C
#endif
#include <windows.h>

static char path_to_dll[_MAX_PATH];

BOOL WINAPI DllMain(HINSTANCE hInstance, DWORD dwReason, void *pv)
{
    if (dwReason == DLL_PROCESS_ATTACH)
    {
        if (GetModuleFileName(hInstance, path_to_dll, _MAX_PATH) == 0)
            return FALSE;
    }
    else if (dwReason == DLL_PROCESS_DETACH)
    {
    }
    return TRUE;
}
#endif
#ifdef __cplusplus
extern "C" {
#endif

static int mclDefaultPrintHandler(const char *s)
{
  return mclWrite(1 /* stdout */, s, sizeof(char)*strlen(s));
}

#ifdef __cplusplus
} /* End extern "C" block */
#endif

#ifdef __cplusplus
extern "C" {
#endif

static int mclDefaultErrorHandler(const char *s)
{
  int written = 0;
  size_t len = 0;
  len = strlen(s);
  written = mclWrite(2 /* stderr */, s, sizeof(char)*len);
  if (len > 0 && s[ len-1 ] != '\n')
    written += mclWrite(2 /* stderr */, "\n", sizeof(char));
  return written;
}

#ifdef __cplusplus
} /* End extern "C" block */
#endif

/* This symbol is defined in shared libraries. Define it here
 * (to nothing) in case this isn't a shared library. 
 */
#ifndef LIB_dis_to_pos_matlab_C_API
#define LIB_dis_to_pos_matlab_C_API /* No special import/export declaration */
#endif

LIB_dis_to_pos_matlab_C_API 
bool MW_CALL_CONV dis_to_pos_matlabInitializeWithHandlers(
    mclOutputHandlerFcn error_handler,
    mclOutputHandlerFcn print_handler)
{
    int bResult = 0;
  if (_mcr_inst != NULL)
    return true;
  if (!mclmcrInitialize())
    return false;
  if (!GetModuleFileName(GetModuleHandle("dis_to_pos_matlab"), path_to_dll, _MAX_PATH))
    return false;
    {
        mclCtfStream ctfStream = 
            mclGetEmbeddedCtfStream(path_to_dll);
        if (ctfStream) {
            bResult = mclInitializeComponentInstanceEmbedded(   &_mcr_inst,
                                                                error_handler, 
                                                                print_handler,
                                                                ctfStream);
            mclDestroyStream(ctfStream);
        } else {
            bResult = 0;
        }
    }  
    if (!bResult)
    return false;
  return true;
}

LIB_dis_to_pos_matlab_C_API 
bool MW_CALL_CONV dis_to_pos_matlabInitialize(void)
{
  return dis_to_pos_matlabInitializeWithHandlers(mclDefaultErrorHandler, 
                                                 mclDefaultPrintHandler);
}

LIB_dis_to_pos_matlab_C_API 
void MW_CALL_CONV dis_to_pos_matlabTerminate(void)
{
  if (_mcr_inst != NULL)
    mclTerminateInstance(&_mcr_inst);
}

LIB_dis_to_pos_matlab_C_API 
void MW_CALL_CONV dis_to_pos_matlabPrintStackTrace(void) 
{
  char** stackTrace;
  int stackDepth = mclGetStackTrace(&stackTrace);
  int i;
  for(i=0; i<stackDepth; i++)
  {
    mclWrite(2 /* stderr */, stackTrace[i], sizeof(char)*strlen(stackTrace[i]));
    mclWrite(2 /* stderr */, "\n", sizeof(char)*strlen("\n"));
  }
  mclFreeStackTrace(&stackTrace, stackDepth);
}


LIB_dis_to_pos_matlab_C_API 
bool MW_CALL_CONV mlxDis_to_pos_matlab(int nlhs, mxArray *plhs[], int nrhs, mxArray 
                                       *prhs[])
{
  return mclFeval(_mcr_inst, "dis_to_pos_matlab", nlhs, plhs, nrhs, prhs);
}

LIB_dis_to_pos_matlab_CPP_API 
void MW_CALL_CONV dis_to_pos_matlab(int nargout, mwArray& xyz, const mwArray& x1, const 
                                    mwArray& x2, const mwArray& x3, const mwArray& x4, 
                                    const mwArray& x5, const mwArray& x6, const mwArray& 
                                    x7, const mwArray& x8, const mwArray& x9, const 
                                    mwArray& x10, const mwArray& x11, const mwArray& x12, 
                                    const mwArray& da, const mwArray& db, const mwArray& 
                                    dc, const mwArray& dd)
{
  mclcppMlfFeval(_mcr_inst, "dis_to_pos_matlab", nargout, 1, 16, &xyz, &x1, &x2, &x3, &x4, &x5, &x6, &x7, &x8, &x9, &x10, &x11, &x12, &da, &db, &dc, &dd);
}

