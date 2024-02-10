import SideNav from "@/components/SideNav";
// import {AdminTable, AcademicTable, ClassTable, InvoiceTable} from "@/components/Table";


export default function Layout({ children }: { children: React.ReactNode }) {
  return (
    <div className="flex h-screen flex-row md:overflow-hidden">
      <div className="w-full flex-none w-24 md:w-64">
        <SideNav />
      </div>
      {/* <Table/> */}
      <div className="flex-grow p-6 md:overflow-y-auto md:p-12">{children}
      {/* <AdminTable/>
      <AcademicTable/>
      <ClassTable/>
      <InvoiceTable/> */}
      </div>
    </div>
  );
}