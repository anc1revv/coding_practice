import co.actioniq.thrift.query._
import co.actioniq.thrift.segment._
import co.actioniq.thrift.query.FilterTypeAliases._

thriftSQL("select recursive_thrift from query_api.persisted_segment_definition where recursive_thrift is not null and customer$id =1 and id = 1650 limit 1", CompositeSegmentNode)

//Union Type Getter Methods
def get_simple_def(a:CompositeNodeType) : Option[SimpleSegmentDefinition] = {
   a match {
      case CompositeNodeType.Simple (s) => Some(s)
      case _ => None
   }
}

def get_compare_alias_option(a:FilterType) : Option[CompareAlias] = {
   a match { 
    case FilterType.Compare (c) => Some(c)
    case _ => None
  }
}


def get_variables_from_audience(a:CompositeSegmentNode) : Seq[VariableFilter] = {
   return get_simple_def(a.nodeType).map(_.filters).getOrElse(Nil);}


def variable_has_empty_compr(a:CompositeSegmentNode) : Boolean = {
   var variables = get_variables_from_audience(a)
   for (variable <- variables){

      get_compare_alias_option(variable.filterType)
        .foreach { x => if (x.op == CompareOp.Empty) return true }
   }
   return false
}

// Grab the seq from the thriftSQL output and apply the variable_has_empty_compr function to it.
res0.filter(variable_has_empty_compr)
